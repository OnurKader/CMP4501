# BAU CMP4501
___
#### Bahçeşehir University CMP4501 Spring Term Project
___

| Name | ID |
| ---- | --- |
| Onur Orkun Kader | 1728778 |

cd into search
`cd search/`

Functions to Run

```shell
python2 pacman.py -l tinyMaze -p SearchAgent
python2 pacman.py -l mediumMaze -p SearchAgent
pythoni pacman.py -l bigMaze -z 0.66 -p SearchAgent
python2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python2 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z 0.66
python2 pacman.py -l bigMaze -p SearchAgent -a fn=astar -z 0.66
python2 eightpuzzle.py
python2 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python2 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python2 pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python2 pacman.py -l openMaze -p SearchAgent -a fn=dfs -z 0.9
python2 pacman.py -l openMaze -p SearchAgent -a fn=bfs -z 0.9
python2 pacman.py -l openMaze -p SearchAgent -a fn=ucs -z 0.9
python2 pacman.py -l openMaze -p SearchAgent -a fn=astar -z 0.9
python2 pacman.py -l bigMaze -z 0.66 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

