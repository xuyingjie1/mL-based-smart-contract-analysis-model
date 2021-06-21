function distributeBTR(address[] address) onlyOwner {
    for (uint i = 0; i < addresses.length; i++){
        balances[owner] -= 2000 * 10**8;
        balances[address[i]] += 2000 * 10**8;
        Transfer(owner, addresses[i], 2000 * 10**8);
    }
}