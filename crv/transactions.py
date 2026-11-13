import vsc

from test_fifo import WIDTH, DEPTH

@vsc.randobj
class FifoTxn:
    def __init__(self, width=WIDTH):
        self.wr_en = vsc.rand_bit_t(1)
        self.rd_en = vsc.rand_bit_t(1)
        self.wr_data = vsc.rand_bit_t(width)
        self.rst = vsc.rand_bit_t(1)
        self.wr_roll = vsc.rand_uint8_t()
        self.rd_roll = vsc.rand_uint8_t()
        self.count = vsc.uint32_t()

    @vsc.constraint
    def rolls_c(self):
        self.wr_roll < 100
        self.rd_roll < 100

    @vsc.constraint
    def reset_c(self):
        vsc.dist(self.rst, [vsc.weight(0, 99), vsc.weight(1, 1)])

    @vsc.constraint
    def occupancy_c(self):
        with vsc.if_then(self.count == 0):
            with vsc.implies(self.wr_roll < 80):
                self.wr_en == 1
            with vsc.implies(self.wr_roll >= 80):
                self.wr_en == 0
            with vsc.implies(self.rd_roll < 25):
                self.rd_en == 1
            with vsc.implies(self.rd_roll >= 25):
                self.rd_en == 0
        with vsc.else_if(self.count == DEPTH):
            with vsc.implies(self.rd_roll < 80):
                self.rd_en == 1
            with vsc.implies(self.rd_roll >= 80):
                self.rd_en == 0
            with vsc.implies(self.wr_roll < 25):
                self.wr_en == 1
            with vsc.implies(self.wr_roll >= 25):
                self.wr_en == 0
        with vsc.else_then:
            with vsc.implies(self.wr_roll < 60):
                self.wr_en == 1
            with vsc.implies(self.wr_roll >= 60):
                self.wr_en == 0
            with vsc.implies(self.rd_roll < 60):
                self.rd_en == 1
            with vsc.implies(self.rd_roll >= 60):
                self.rd_en == 0
