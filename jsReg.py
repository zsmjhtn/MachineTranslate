# -*- coding:UTF-8 -*-
import execjs


class jsReg():
    def __init__(self):
        self.ctx = execjs.compile("""
        function reg(t) {
            return t.replace(/\\n(\\n?)/g, '$1$1')
        }
    """)

    def get_reg_text(self, t):
        return self.ctx.call('reg', t)
