from mcrcon import MCRcon

with MCRcon("66.235.175.113","pass") as mcr:
    resp = mcr.command("say test again")
    print(resp)
#test push 2