#!/usr/bin/env bash

function _test_fail() {
  echo FAIL
  [[ -z $VERBOSE_DIFF ]] && \
    printf "  To know more:\\n  VERBOSE_DIFF=1 %s %s\\n" \
      "$(basename $0)" "$test_name"
}

function _test_ok() {
    echo OK
}

function run_single_test() {
  local test_name="$1"; shift
  local bash="$1"; shift
  local python="$1"; shift

  local test_bash="test_$test_name.bash"
  local test_python="test_$test_name.py"

  printf "\\n-- [ %s ] --\\n" "$test_name"

  if [[ ! -f "$test_bash" ]] || [[ ! -f "$test_python" ]]; then
    echo "> File(-s) for test '$test_name' not found" >&2
    _test_fail
    return
  fi

  if [[ -z $VERBOSE_DIFF ]]; then
    diff -q \
      <("$bash" "$test_bash") <("$python" "$test_python") >/dev/null 2>&1
  else
    diff --side-by-side --expand-tabs \
      <("$bash" "$test_bash") <("$python" "$test_python")
  fi

  [[ $? -eq 0 ]] && _test_ok || _test_fail
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
    # 'should_fail'
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
