
class Solution {
public:
    // Function to merge nums2 into nums1 in-place
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // 'last' will point to the last index of the merged array
        int last = m + n - 1;

        // both arrays have elements left to compare
        while (m > 0 && n > 0) {
            // Compare the last valid elements of both arrays
            if (nums1[m - 1] > nums2[n - 1]) {
                // If nums1 element is greater, place it at the 'last' position
                nums1[last] = nums1[m - 1];
                m--;  // Move nums1 pointer back
            } else {
                // Otherwise, place nums2 element at the 'last' position
                nums1[last] = nums2[n - 1];
                n--;  // Move nums2 pointer back
            }
            last--; // Move the last pointer backward for the next placement
        }

        // If any elements are left in nums2 (nums1 might be already done)
        while (n > 0) {
            nums1[last] = nums2[n - 1];
            n--;
            last--;
        }
    }
};


