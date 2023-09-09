def kilekotte(arv):
    if arv == 0:
        return 0
    else:
        if (arv - 1) % 3 == 0:
            return kilekotte(arv - 1) + 2
        else:
            return kilekotte(arv - 1) + 1
        
print(kilekotte(1))
            