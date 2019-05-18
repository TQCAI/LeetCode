package ValidParentheses;

import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();
        String left = "{[(";
        String right = "}])";
        for (int i = 0; i < s.length(); i++) {
            String c = s.substring(i, i + 1);
            int leftIndex = left.indexOf(c);
            if (leftIndex >= 0) {
                stack.push(c);
            } else {
                boolean ans = stack.size() > 0 && left.indexOf(stack.peek()) == right.indexOf(c);
                if (!ans)
                    return false;
                else {
                    stack.pop();
                }
            }
        }
        return stack.size() == 0;
    }

    public static void main(String[] args) {
        String array[] = new String[]{"(]", "{[()]}"};
        for (String s : array) {
            boolean ans = new Solution().isValid(s);
            System.out.println(ans);
        }

    }
}