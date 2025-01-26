Binary Euclidean Algorithm, this approach is use for large numbers, as  it reduces number of division and also more efficient for low level languages that involve manipulation of bits
BinaryGCD(a, b)
    If a = 0 then
        return b
    If b = 0 then
        Return a
    bits = 0
    While (a is even) and (b is even) 
        a = a / 2
        b = b / 2
        bits + = 1
   End While 
#now a becomes odd and b is even
    While (a is even) do
        a = a / 2
    End While
    While (b not equal to 0)
        While (b is even) 
            b = b / 2
        
        # both a and b are odd
        If a > b 
            a = (a - b) / 2
        Else
            b = (b - a) / 2
          End While
    End While
    Return  a x 2^k  
End Function
