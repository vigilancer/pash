uname -a | \
  awk 'BEGIN { RS=" " }; { print $1; }' | \
  sort | \
  head -3

ls -1 | wc -l | tr -d ' '
