def kilekotte(arv):
    if arv == 1:
        return 2
    else:
        if (arv - 1) % 3 == 0:
            return kilekotte(arv - 1) + 2
        else:
            return kilekotte(arv - 1) + 1
        
print(kilekotte(8))
            