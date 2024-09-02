class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        csum=0
        for i in range(len(chalk)):
            csum+=chalk[i]
        count=k % csum
        student=0
        for i in range(len(chalk)):
            if count<chalk[i]:
                student=i
                break
            count-=chalk[i]

        return student