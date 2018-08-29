printf Stdout1 | xargs -I{} echo {} 2>/dev/null
#> Stdout

printf Stdout2 | xargs -I{} echo {} 1>/dev/null
#> 
