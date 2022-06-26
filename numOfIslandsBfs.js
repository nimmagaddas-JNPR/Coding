const directions = [[1,0], [-1,0], [0,1], [0,-1]]

var numIslands = function(grid) {
    if (grid.length === 0) { return [] } //base case
    
    const ROWS = grid.length
    const COLS = grid[0].length
    
    let islandCount = 0
    
    function bfs(r, c) {
        let queue = [];

        queue.push([r,c])
        grid[r][c] = '0' // mark it as visited

        while(queue.length !== 0) {
            let [row, col] = queue.shift();

            for (const [dr,dc] of directions) {  //process neighbors
                let r = row + dr,
                    c = col + dc

                if (r >= 0 && c >= 0 
                    && r < ROWS && c < COLS
                    && grid[r][c] === '1') {
                    queue.push([r,c]) // add to queue and 
                    grid[r][c] = '0'  // mark as visited
                }
            }

        }
    
    }
    
    for (let r=0; r<ROWS; r++) {
        for (let c=0; c<COLS; c++) {
            if (grid[r][c] === '1') {
                bfs(r, c)
                islandCount++
            }
        }   
    }
    
    return islandCount
}

