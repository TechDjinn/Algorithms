function main(){
    let number = 6;
    console.log(factorial_recursive(number));
}

function factorial_recursive(number){
    if (number <= 1){
        return 1;   // Base case
    } else {
        return number * factorial_recursive(number - 1);
    }
}

main();