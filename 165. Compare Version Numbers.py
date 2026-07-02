class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versiononesplit=[int(value) for value in version1.split(".") ]
        versiontwosplit = [int(value) for value in version2.split(".")]
        for i in range(max(len(versiononesplit),len(versiontwosplit))):
            v1=versiononesplit[i] if i<len(versiononesplit) else 0
            v2=versiontwosplit[i] if i<len(versiontwosplit) else 0
            if v1>v2:
                return 1
            elif v2 > v1:
                return -1
        return 0
                
        
