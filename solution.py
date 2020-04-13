from collections import Counter


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    # recursively search for all combination of numbers (with repetition),
    # whose sum equals is equal to target (or less)
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = set()
        intermedia = []
        self.recursion(candidates, target, res, intermedia)
        return [list(i) for i in res]

    def recursion(self, candidates, target, res, intermedia):
        for i in candidates:
            if target == i:
                temp = intermedia + [i]
                temp.sort()
                if temp is not None:
                    res.add(tuple(temp))
                return
            elif target > i:
                self.recursion(candidates, target - i, res, intermedia + [i])
            else:
                return


def get_orders():
    """
       get input from console
       :return: dictionary of orders: {'VS5': 3, 'CF': 10, ..}
    """
    lines = []
    orders = {}
    # get lines until empty line seen
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    try:
        for el in lines:
            lst = el.split(' ')
            orders[lst[1]] = int(lst[0])
    except:
        print("Wrong input. Please try again!")
    return orders


def get_optimal_packs(num, pack_types):
    """

    :param num: number of items ordered
    :param pack_types: sorted list (asc) of package sizes for an item
    :return: Counter object with (key, value) => (pack type, number of packs)
    """
    test = Solution()  # call the Combination of Sums class
    # list of combinations of numbers whose sum is <= order input
    results = test.combinationSum(pack_types, num)
    min = len(results[0])
    answer = results[0]
    for el in results[1:]:
        if (len(el) <= min):
            min = len(el)
            answer = el
    return Counter(answer)


def process_order(num, code, packs):
    """
    processes one order and returns the output in a formatted string
    :param num: number of items ordered
    :param code: code of the item ordered
    :param packs: dictionary with the
    :return: formatted string with the output for one single item ordered
    """
    output = ""
    try:
        pack_types = sorted(list(packs[code].keys()))
        optimal_pack = get_optimal_packs(num, pack_types)
        total_cost = 0
        for pack_size, n in optimal_pack.items():
            cost = packs[code][pack_size]
            output += "      " + str(n) + " x " + str(pack_size) + " $" + str(cost) + "\n"
            total_cost += n * cost

        output = str(num) + " " + code + ' $' + str(round(total_cost, 2)) + "\n" + output
    except:
        print("Please try again! Incorrect input/Unavailable item code/ or Number ordered too small.")
    return output
