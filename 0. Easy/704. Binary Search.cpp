class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) {
            left = mid + 1;
        }
        else {
            right = mid;
        }
    }

    if (left > 0 and nums[left - 1] == target) {
        return left - 1;
    }
    else {
        return -1;
    }
    }
};