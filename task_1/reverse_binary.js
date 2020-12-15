function reverseBinary(number) {
    const binaryReverse = number.toString(2).split('').reverse().join('')
    return parseInt(binaryReverse, 2)
}

module.exports = {
    reverseBinary
}


