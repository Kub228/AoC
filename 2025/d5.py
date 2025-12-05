inpt='''3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32'''.split()

# with open("txt_files\\d5.txt") as f:
#   inpt = f.read().split()

# ids=[int(x) for x in inpt if '-' not in x]
rng_of_ids=[x for x in inpt if '-' in x]

rng_of_ids=[x.split('-') for x in rng_of_ids]
rng_of_ids=[(int(x[0]), int(x[1])) for x in rng_of_ids]

print(rng_of_ids)
# print(ids)

def is_fresh_p1(ids,rng_of_ids):
    frsh_ids=[]
    for i in rng_of_ids:
        for k in ids:
            if i[0] <= k <= i[1] and k not in frsh_ids:
                frsh_ids.append(k)
    return len(frsh_ids)


def is_fresh_p2(rng_of_ids):
    #Version 1 O^3 complexity
    # frsh_ids=[]
    # for i in rng_of_ids:
    #     for j in range(i[0],i[1]+1):
    #         for k in rng_of_ids:
    #             if k[0] <= j <= k[1] and j not in frsh_ids:
    #                 frsh_ids.append(j)
    # return len(frsh_ids)

    #Version 2 O^2 complexity
    # ans = []
    # for i in rng_of_ids:
    #     a=[x for x in range(i[0],i[1]+1)]
    #     ans = list(set(ans).union(set(a)))

    # return len(ans)

    ans=[]
    for i in rng_of_ids:
        pass



# print(is_fresh_p1(ids,rng_of_ids))
print(is_fresh_p2(rng_of_ids))