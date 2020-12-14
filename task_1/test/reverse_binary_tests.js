const { expect } = require("chai")
const { describe } = require("mocha")
const { convert } = require("../reverse_binary")

describe('reverse binary test', () => {
    it('should return a number which is the binary reverse of the number given', () => {
        expect(convert(13)).to.equal(11)
    })
})
