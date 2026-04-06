bool isPalindrome(int x) {
    if(x < 0){
        return false;
    }
    long long reverse = 0;
    int digit;
    int original = x;
    while(x >0){
        digit = x%10;
        reverse = reverse*10 + digit;
        x = x/10;
    }

    return original == reverse;
}