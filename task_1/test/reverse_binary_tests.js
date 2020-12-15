const { expect } = require("chai")
const { describe } = require("mocha")
const { reverseBinary } = require("../reverse_binary")

describe('reverse binary tests', () => {

    it('should return 0 when the number to reverse binary is 0', () => {
        expect(reverseBinary(0)).to.equal(0)
    })

    it('should return 1 when the number to reverse binary is 1', () => {
        expect(reverseBinary(1)).to.equal(1)
    })

    it('should return 11 when the number to reverse binary is 13', () => {
        expect(reverseBinary(13)).to.equal(11)
    })

    it('should return NaN when the input provided is not a number', () => {
        expect(reverseBinary('foo')).to.be.NaN
    })
})
