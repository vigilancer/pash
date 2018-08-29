#!/usr/bin/env bash

function _test_output() {
  local test_name="$1"; shift
  local bash="$1"; shift
  local python="$1"; shift

  local test_bash="test_$test_name.bash"
  local test_python="test_$test_name.py"

  if [[ -z $VERBOSE_DIFF ]]; then
    diff -q \
      <("$bash" "$test_bash") <("$python" "$test_python") >/dev/null 2>&1
  else
    diff --side-by-side --expand-tabs \
      <("$bash" "$test_bash") <("$python" "$test_python")
  fi

  if [[ $? -eq 0 ]]; then
    printf "Output:\\t\\t OK\\n"
  else
    printf "Output:\\t\\t FAIL\\n"
    [[ -z $VERBOSE_DIFF ]] && \
      printf "  To know more:\\n  VERBOSE_DIFF=1 %s %s\\n" \
        "./$(basename $0)" "$test_name"
  fi
}

function _test_exit_code() {
  local test_name="$1"; shift
  local bash="$1"; shift
  local python="$1"; shift

  local test_bash="test_$test_name.bash"
  local test_python="test_$test_name.py"

  cmd=( "$bash" "$test_bash" )
  "${cmd[@]}" >/dev/null 2>&1
  bash_code=$?

  cmd=( "$python" "$test_python" ">/dev/null 2>&1" )
  "${cmd[@]}" >/dev/null 2>&1
  python_code=$?

  if [[ $bash_code -eq $python_code ]]; then
    printf "Codes:\\t\\t OK\\n"
  else
    printf "Codes:\\t\\t FAIL\\n"
  fi
}


function _print_env() {
  local bash="$1"; shift
  local python="$1"; shift

  echo "Testing env:"
  echo "Bash: $bash"
  echo "Python: $python"
}

function main() {
  local test_names=(
    'pipes_smoke'
    'redirections'
    'assignment'
    'shellfail'
    #'pipefail'  #nut working
    'should_fail'
  )
  [[ $# -ne 0 ]] && test_names=($@)

  local bash_path=$(which bash)
  local python_path=$(which python3)

  _print_env "$bash_path" "$python_path"

  for test_name in "${test_names[@]}"; do
    printf "\\n-- [ %s ] --\\n" "$test_name"

    _test_output "$test_name" "$bash_path" "$python_path"
    _test_exit_code "$test_name" "$bash_path" "$python_path"
  done
}

main "$@"
