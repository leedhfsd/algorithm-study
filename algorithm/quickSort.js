
const quickSort = function(arr, left, right) {
  if (left < right) {
    let pos = divide(arr, left, right);
    quickSort(arr, left, pos - 1);
    quickSort(arr, pos + 1, right);
  }
  return arr;
};

const divide = function(arr, left, right) {
  let i = left;
  let j = right;
  let pivot = arr[left];

  while (i < j) {
    while (arr[j] > pivot) j--;
    while (i < j && arr[i] <= pivot) i++;
    tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
  }
  arr[left] = arr[j];
  arr[j] = pivot;
  return j;
}

console.log(quickSort(input, 0, N-1));
