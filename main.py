def find_missing_ranges(frames):
    if not frames:
        return {"missing_count": 0, "gaps": [], "longest_gap": []}
    
    gaps = []
    missing_count = 0
     
    for i in range(len(frames) - 1):
        current = frames[i]
        next_frame = frames[i + 1]
        
        if next_frame - current > 1: 
            gap_start = current + 1
            gap_end = next_frame - 1
            gaps.append([gap_start, gap_end])
            missing_count += gap_end - gap_start + 1
     
    longest_gap = []
    if gaps:
        longest_gap = gaps[0]  
        longest_size = gaps[0][1] - gaps[0][0]
        
        for gap in gaps:
            gap_size = gap[1] - gap[0]
            if gap_size > longest_size:
                longest_size = gap_size
                longest_gap = gap
    
    return {
        "missing_count": missing_count,
        "gaps": gaps,
        "longest_gap": longest_gap
    }
 
print(find_missing_ranges([1, 2, 3, 5, 6, 10, 11, 16]))
