// Swap between two elements in an array

var swap = function(array, firstIndex, secondIndex) {
  var temp;
  temp = array[firstIndex];
  array[firstIndex] = array[secondIndex];
  array[secondIndex] = temp;
};

var testArray = [7, 9, 4];
swap(testArray, 0, 1);
console.log(testArray);

// Takes an array and a number startIndex, and returns the index of the smallest
// value that occurs with index startIndex or greater. If this smallest value
// occurs more than once in this range, then return the index of the leftmost
// occurrence within this range.

var indexOfMinimum = function(array, startIndex) {
    // Set initial values for minValue and minIndex,
    // based on the leftmost entry in the subarray:  
    var minIndex = startIndex;

    // Loop over items starting with startIndex, 
    // updating minValue and minIndex as needed:
    for(var i = startIndex + 1; i < array.length; i++){
        if(array[minIndex] > array[i]){
            minIndex = i;
        }
    }
    
    return minIndex;
}; 

var array = [18, 6, 66, 44, 9, 22, 14];   
var index = indexOfMinimum(array, 2);

//  For the test array [18, 6, 66, 44, 9, 22, 14], 
//  the value 9 is the smallest of [..66, 44, 9, 22, 14]
//  Since 9 is at index 4 in the original array, 
//  "index" has value 4
console.log("The index of the minimum value of the subarray starting at \
            index 2 is " + index + "."  );


// Implement selection sort

var selectionSort = function(array) {
    var index_min;
    for(var i = 0; i < array.length; i++){
        index_min = indexOfMinimum(array, i);
        swap(array, i, index_min);   
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
console.log("Array after sorting: " + array);
