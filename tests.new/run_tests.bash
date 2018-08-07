#!/usr/bin/env bash

function run_single_test() {
  local test_name="$1"; shift
  local bash="$1"; shift
  local python="$1"; shift

  local test_bash="test_$test_name.bash"
  local test_python="test_$test_name.py"

  echo "-- [ $test_name ] --"

  if [[ -z $VERBOSE_DIFF ]]; then
    diff -q \
      <("$bash" "$test_bash") <("$python" "$test_python") >/dev/null 2>&1
  else
    diff --side-by-side --expand-tabs \
      <("$bash" "$test_bash") <("$python" "$test_python")
  fi

  if [[ $? -eq 0 ]]; then
    echo OK
  else
    echo FAIL
    [[ -z $VERBOSE_DIFF ]] && \
      printf "To know more:\\nVERBOSE_DIFF=1 %s %s\\n" \
        "$(basename $0)" "$test_name"
  fi
}

function _print_env() {
  local bash="$1"; shift
  local python="$1"; shift

  echo 'Testing env:'
  echo "Bash: $bash"
  echo "Python: $python"
}

function main() {
  local test_names=(
    'smoke'
    #'should_fail'
    'pipes_output'
  )
  [[ $# -ne 0 ]] && test_names=($@)

  local bash_path=$(which bash)
  local python_path=$(which python3)

  _print_env "$bash_path" "$python_path"

  for test_name in "${test_names[@]}"; do
    run_single_test "$test_name" \
      "$bash_path" "$python_path"
  done
}

main "$@"
