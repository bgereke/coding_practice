# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

 

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

# Constraints:

# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.

# my original solution
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         letter_logs = []
#         letter_log_words = []
#         letter_log_ids = []
#         digit_logs = []
#         s = ' '
#         num_letter_logs = 0
#         for i, log in enumerate(logs):
#             split_log = log.split()
#             if split_log[1].isnumeric():
#                 digit_logs.append(log)
#             else:
#                 num_letter_logs += 1
#                 log_words = s.join(split_log[1:])
#                 for j, words in enumerate(letter_log_words):
#                     if log_words < words:
#                         letter_logs.insert(j, log)
#                         letter_log_words.insert(j, log_words)
#                         letter_log_ids.insert(j, split_log[0])
#                         break
#                     elif log_words == words and split_log[0] < letter_log_ids[j]:
#                         letter_logs.insert(j, log)
#                         letter_log_words.insert(j, log_words)
#                         letter_log_ids.insert(j, split_log[0])
#                         break
#                 if num_letter_logs > len(letter_logs):
#                     letter_logs.append(log)
#                     letter_log_words.append(log_words)
#                     letter_log_ids.append(split_log[0])
#         return letter_logs + digit_logs

# more elegant solution (provided; tested at similar performance)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key) 