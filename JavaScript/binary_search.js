function main(){
    let arr = [
        11, 16, 17, 22, 25, 29, 32, 35, 
        37, 37, 39, 40, 44, 50, 59, 60, 
        60, 60, 61, 62, 65, 67, 70, 80,
        81, 81, 82, 90, 92, 93, 94, 99
        ];

    let n = 50;

    if (binary_search(n, arr) === true){
        console.log("Element found!");
    } else{
        console.log("Element NOT found!");
    }
}

function binary_search(element_to_find, array_to_search){
    let low = 0;
    let high = array_to_search.length;

    while (low <= high){
        let mid = Math.floor((low + high) / 2);

        if (array_to_search[mid] === element_to_find){
            return true;
        } else if (array_to_search[mid] > element_to_find){
            high = mid - 1;
        } else{
            low = mid + 1;
        }
    }

    return false;
}

main();