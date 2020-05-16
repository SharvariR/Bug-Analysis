# Bug-Analysis
The project involves analysis of bugs to find frequency, priority, hierarchy of bugs, We can determine most abundant bug and least abundant bug as well. The algorithm eventually creates the tree of bugs as per the hierarchy and inputs of bug report.

Overview:
We have n bugs reported by the system in the form of bug report and there parent causes. We need to analyze it to get the occurances hierarchy, abundancy, root issues, new issues etc. There can be a case where a bug is entirely generated from a single parent or from multiple. Also the generated bug may have some contribution of the parent bugs.

Inputs: 
Reading a TSV (Tab Separated Values) file as a bug report :
bug_id: bug indicative id number
parent_bug_id: id of the bug which created given bug_id in the row
occurrences: Number of times bug occures in system . Null in case of non leaf bugs.
percentage_contribution: The number of times a bug arises from parent bug out of 100 times.
