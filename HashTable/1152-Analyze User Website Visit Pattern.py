class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        def helper(sol,idx,res,arr):
            if len(sol)==3:
                res.add(tuple(sol))
                return 
            for i in range(idx,len(arr)):
                helper(sol+[arr[i]],i+1,res,arr)
                
        def getseq3(arr):#get all unique 3 sequence tuple list from array of events
            res=set()
            helper([],0,res,arr)
            return res    
        
        people2weblis=collections.defaultdict(list)
        seq3Cnt=collections.Counter()
        for _,user,ws in sorted(zip(timestamp,username,website)):
            people2weblis[user].append(ws)
        for weblis in people2weblis.values():
            for seq3 in getseq3(weblis):
                seq3Cnt[seq3]+=1
        return min(seq3Cnt,key=lambda k:[-seq3Cnt[k],k])