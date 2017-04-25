###############################################################################
# given a string as input and a substring , find how many times that substring
# exists in the given string
###############################################################################


class Findsubstring():

    def __init__(self, string, substring):
        self.string = string
        self.substring = substring

    def count_substring(self):
        '''
        returns the count of
        substring
        '''
        count = 0
        for i in range(len(self.string)-len(self.substring)+1):
            if self.string[i:i+len(self.substring)] == self.substring:
                count += 1
        return count


substring_count = Findsubstring('rupesheshkanto', 'esh')
print(substring_count.count_substring())
