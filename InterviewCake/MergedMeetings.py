import unittest

def merge_meetings(meetings):

    sortedMeetings = sorted(meetings)

    mergedMeetings = [sortedMeetings[0]]

    for current_meeting_start, current_meeting_end in sortedMeetings[1:]:
        last_meeting_start, last_meeting_end = mergedMeetings[-1]

        if current_meeting_start <= last_meeting_end:
            mergedMeetings[-1] = last_meeting_start , max(current_meeting_end, last_meeting_end)
        else:
            mergedMeetings.append((current_meeting_start, current_meeting_end))
    return mergedMeetings

class TestCase(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(merge_meetings([(1, 10), (2, 6), (3, 5), (7, 9)]), [(1,10)])
    def testcase2(self):
        self.assertEqual(merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]), [(0, 1), (3, 8), (9, 12)])
if __name__ == "__main__":
    unittest.main()
