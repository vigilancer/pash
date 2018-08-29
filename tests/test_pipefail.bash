
# disable pipefail
set +o pipefail

false | true
printf 'Heyho\n'

# enable pipefail
set -o pipefail

false | true
