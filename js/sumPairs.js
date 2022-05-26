exports.sumPairs = function() {
    let result = [];
    for (let i = 0; i < Array.length - 1; i++) {
        for (let j = i + 1; j < Array.length; j++) {
            if (arr[i] + arr[j] === num) {
                result.push([arr[i], arr[j]]);
            }
        }
    }
    if (result.length === 0) return 'Unable to find pairs.'
    else return result;
};
