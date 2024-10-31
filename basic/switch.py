class A:
    def case1(self):
        return "This is case 1"

    def case2(self):
        r = "This is case 2"
        print(r)
        return r

    def case3(self):
        r = "This is case 3"
        print(r)
        return r

    def default(self):
        return "No case matched"

    def p(self):
        switch_dict = {
            'case1': self.case1(),
            'case2': self.case2,
            'case3': self.case3
        }
        result = switch_dict.get('case2', self.default)()
        # result = simulate_switch('case2')
        print(result)  # 输出: This is case 2

    def simulate_switch(value):
        return


if __name__ == '__main__':
    a = A()
    a.p()

