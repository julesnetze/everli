function convert(number) {
    let binary_reverse = number.toString(2).split('').reverse().join('')
    return parseInt(binary_reverse, 2)
}

module.exports = {
    convert
}


