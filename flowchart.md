main:
            [start]
               |
          [input: num]
               |
     [output = prettify(num)]
               |
        [print(output)]
               |
             [stop]


prettify:
            [start]             
               |
          [num[::-1]]
               |
    [iterate  through      the] 
    [number and count to three]
    [if the counter = 3  then ]
    [add comma  and  make  the]
    [value of counter equals 0]
    [and delete the last comma]
               |
      [add  these  into a]
      [list and join them]
      [and  reverse  them]
               |
    [return the final result]