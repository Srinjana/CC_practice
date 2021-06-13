# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit.
# Input:
# N = 7
# arr[] = {6, 2, 5, 4, 5, 1, 6}
# Output: 12
class Solution():
    def getmaxarea(self, histogram):
        stack = list()

        max_area = 0  # Initialize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(histogram):

            # If this bar is higher
            # than the bar on top of
            # stack, push it to stack

            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (histogram[top_of_stack] *
                        ((index - stack[-1] - 1)
                        if stack else index))

                # update max area, if needed
                max_area = max(max_area, area)

        # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:

            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                    if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

        # Return maximum area under
        # the given histogram
        return max_area

if __name__ == '__main__':
    n = int(input())
    
    a = list(map(int, input().strip().split()))

    ob = Solution()
    print (ob.getmaxarea(a))
    # print(len(a))

