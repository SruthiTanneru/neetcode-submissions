class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output_list = []
        for i in range(len(operations)):
            curr_element = operations[i]
            if curr_element == "+":
                output_list.append((int(output_list[-1]) + int(output_list[-2])))
            elif curr_element == "D":
                output_list.append(int(output_list[-1]*2))
            elif curr_element == "C":
                output_list.pop()
            else:
                output_list.append(int(curr_element))
        
        
        total = sum(output_list)
        return total

        