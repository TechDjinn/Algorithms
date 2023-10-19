function main(){
    let n = 6;
    console.log(factorial_recursive(n));
}

function factorial_recursive(n){
    if (n <= 1){
        return 1;
    } else {
        return n * factorial_recursive(n-1);
    }
}

main();