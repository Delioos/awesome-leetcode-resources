use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        let mut map = HashMap::new();
        map.insert(')', '(');
        map.insert('}', '{');
        map.insert(']', '[');
        
        for c in s.chars() {
            if c == '(' || c == '{' || c == '[' {
                stack.push(c);
            } else if c == ')' || c == '}' || c == ']' {
                if let Some(&opening) = map.get(&c) {
                    if stack.pop() != Some(opening) {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        
        stack.is_empty()
    }
}
