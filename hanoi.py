def hanoi(n, src, aux, des):
    if n == 1:
        print(f"Move disk 1 from {src} to {des}")
        return

    hanoi(n-1, src, des, aux)
    print(f"Move disk {n} from {src} to {des}")
    hanoi(n-1, aux, src, des)

n = 3

src_rd = 'A'
aux_rd = 'B'
des_rd = 'C'

hanoi(n, src_rd, aux_rd, des_rd)
            

            
