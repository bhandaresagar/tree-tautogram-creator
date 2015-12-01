# !/usr/bin/python

__author__ = 'sagar, chitesh'

'''
Analysis for Totogram (Programming Question - 2.2)

Best solution with time:

1. height = 3

Time taken:  0.0001  seconds
Maximum difference: 3
Totogram Tree: 5 2 6 8 1 3 4 7 9 10

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 3.png]

2. height = 4

Time taken:  0.00014 seconds
Maximum difference: 4
Totogram Tree: 11 7 12 15 3 4 9 14 18 19 1 2 6 5 8 10 13 16 20 17 21 22

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 4.png]

3. height = 5

Time taken:  0.00022 seconds
Maximum difference: 6
Totogram Tree: 23 17 24 29 11 12 19 28 34 35 5 6 10 7 16 21 26 31 39 37 40 41 1 2 4 3 13 14 9 8 15 18 20 22 25 27 30 32 42 38 33 36 44 43 45 46

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 5.png]

4. height = 6

Time taken:  0.00052 seconds
Maximum difference: 10
Totogram Tree: 47 37 48 57 27 28 39 56 66 67 17 18 22 19 34 43 52 61 75 73 76 77 7 8 10 9 23 26 16 13 32 36 41 45 50 54 59 63 82 79 69 72 85 88 86 87 1 2 4 3 11 12 6 5 24 25 30 29 20 21 15 14 31 33 35 38 40 42 44 46 49 51 53 55 58 60 62 64 81 80 74 78 68 65 70 71 90 89 83 84 92 91 93 94

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 6.png]

5. height = 7

Time taken:  0.00257 seconds
Maximum difference: 16
Totogram Tree: 95 79 96 111 63 64 78 113 126 127 47 48 43 49 70 87 104 121 141 148 142 143 31 32 19 33 44 54 36 34 66 74 83 91 100 108 117 125 156 155 137 147 157 176 158 159 15 16 7 17 20 23 12 18 45 51 58 55 37 40 29 26 62 68 72 76 81 85 89 93 98 102 106 110 115 119 123 129 165 162 151 154 136 133 140 146 172 179 168 171 173 184 174 175 1 2 4 3 8 9 6 5 21 22 25 24 13 14 11 10 46 50 53 52 59 60 57 56 38 39 42 41 30 35 28 27 61 65 67 69 71 73 75 77 80 82 84 86 88 90 92 94 97 99 101 103 105 107 109 112 114 116 118 120 122 124 128 130 164 163 160 161 150 149 152 153 135 134 131 132 139 138 144 145 181 180 177 178 167 166 169 170 186 185 182 183 188 187 189 190

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 7.png]

6. height = 8

Time taken:  0.01253  seconds
Maximum difference: 28
Totogram Tree: 191 163 192 219 135 136 158 225 246 247 107 108 91 109 142 175 208 241 273 292 274 275 79 80 39 81 92 110 72 82 132 150 167 183 200 216 233 251 300 311 276 291 301 344 302 303 51 52 15 53 40 47 32 54 93 100 118 111 73 84 65 58 128 138 146 154 162 171 179 187 196 204 212 221 229 237 245 255 325 318 299 310 272 265 283 290 328 351 336 343 329 368 330 331 23 24 7 25 16 19 12 26 41 44 55 48 33 36 29 27 94 97 104 101 119 122 115 112 74 77 88 85 66 69 62 59 126 130 134 140 144 148 152 156 160 165 169 173 177 181 185 189 194 198 202 206 210 214 218 223 227 231 235 239 243 249 253 257 324 321 314 317 298 295 306 309 271 268 261 264 282 279 286 289 355 354 347 350 335 332 339 342 356 371 364 367 357 376 358 359 1 2 4 3 8 9 6 5 17 18 21 20 13 14 11 10 42 43 46 45 56 57 50 49 34 35 38 37 30 31 28 22 95 96 99 98 105 106 103 102 120 121 124 123 116 117 114 113 75 76 83 78 89 90 87 86 67 68 71 70 63 64 61 60 125 127 129 131 133 137 139 141 143 145 147 149 151 153 155 157 159 161 164 166 168 170 172 174 176 178 180 182 184 186 188 190 193 195 197 199 201 203 205 207 209 211 213 215 217 220 222 224 226 228 230 232 234 236 238 240 242 244 248 250 252 254 256 258 323 322 319 320 313 312 315 316 297 296 293 294 305 304 307 308 270 269 266 267 260 259 262 263 281 280 277 278 285 284 287 288 361 360 352 353 346 345 348 349 334 333 326 327 338 337 340 341 373 372 369 370 363 362 365 366 378 377 374 375 380 379 381 382

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 8.png]

7. height = 9

Time taken:  0.09031  seconds
Maximum difference: 48
Totogram Tree: 383 335 384 431 287 288 318 449 478 479 239 240 183 241 284 351 416 483 525 584 526 527 191 192 82 193 184 219 152 194 268 302 334 367 400 433 465 499 572 615 548 583 573 685 574 575 143 144 34 145 83 103 67 146 185 204 235 220 153 168 132 147 260 276 294 310 326 343 359 375 392 408 424 441 457 473 491 507 619 635 599 614 547 532 563 582 620 700 664 684 621 733 622 623 95 96 15 97 35 42 27 98 84 91 111 104 68 75 60 99 186 197 212 205 236 246 228 221 154 161 176 169 133 140 125 118 256 264 272 280 290 298 306 314 322 330 339 347 355 363 371 379 388 396 404 412 420 428 437 445 453 461 469 477 487 495 503 511 649 642 627 634 598 591 606 613 546 539 521 531 562 555 570 581 667 707 692 699 663 656 676 683 668 740 725 732 669 752 670 671 47 48 7 49 16 19 12 50 36 39 46 43 28 31 24 51 85 88 100 92 112 115 108 105 69 72 79 76 61 64 57 54 187 190 201 198 213 216 209 206 237 243 250 247 229 232 225 222 155 158 165 162 177 180 173 170 134 137 149 141 126 129 122 119 254 258 262 266 270 274 278 282 286 292 296 300 304 308 312 316 320 324 328 332 337 341 345 349 353 357 361 365 369 373 377 381 386 390 394 398 402 406 410 414 418 422 426 430 435 439 443 447 451 455 459 463 467 471 475 481 485 489 493 497 501 505 509 513 648 645 638 641 626 618 630 633 597 594 587 590 605 602 609 612 545 542 535 538 520 517 524 530 561 558 551 554 569 566 577 580 713 710 703 706 691 688 695 698 662 659 652 655 675 672 679 682 715 743 736 739 724 721 728 731 716 755 748 751 717 760 718 719 1 2 4 3 8 9 6 5 17 18 21 20 13 14 11 10 37 38 41 40 52 53 45 44 29 30 33 32 25 26 23 22 86 87 90 89 101 102 94 93 113 114 117 116 109 110 107 106 70 71 74 73 80 81 78 77 62 63 66 65 58 59 56 55 188 189 196 195 202 203 200 199 214 215 218 217 210 211 208 207 238 242 245 244 251 252 249 248 230 231 234 233 226 227 224 223 156 157 160 159 166 167 164 163 178 179 182 181 174 175 172 171 135 136 139 138 150 151 148 142 127 128 131 130 123 124 121 120 253 255 257 259 261 263 265 267 269 271 273 275 277 279 281 283 285 289 291 293 295 297 299 301 303 305 307 309 311 313 315 317 319 321 323 325 327 329 331 333 336 338 340 342 344 346 348 350 352 354 356 358 360 362 364 366 368 370 372 374 376 378 380 382 385 387 389 391 393 395 397 399 401 403 405 407 409 411 413 415 417 419 421 423 425 427 429 432 434 436 438 440 442 444 446 448 450 452 454 456 458 460 462 464 466 468 470 472 474 476 480 482 484 486 488 490 492 494 496 498 500 502 504 506 508 510 512 514 647 646 643 644 637 636 639 640 625 624 616 617 629 628 631 632 596 595 592 593 586 585 588 589 604 603 600 601 608 607 610 611 544 543 540 541 534 533 536 537 519 518 515 516 523 522 528 529 560 559 556 557 550 549 552 553 568 567 564 565 576 571 578 579 712 711 708 709 702 701 704 705 690 689 686 687 694 693 696 697 661 660 657 658 651 650 653 654 674 673 665 666 678 677 680 681 745 744 741 742 735 734 737 738 723 722 714 720 727 726 729 730 757 756 753 754 747 746 749 750 762 761 758 759 764 763 765 766

[Generated Tree: <github repo>/Totogram - Trees/Totogram - 9.png]

Algorithm--

Bounded local-search in a closed space for placement of nodes.

Complexity:

1. Finding the maximum absolute difference: O(number of limiting differences evaluated * height of totogram)

Explanation:
Big-O of number of differences evaluated starting from 1 till the maximum absolute difference found multiplied by height of the totogram

2. Constructing the Totogram: O(number of elements in left-subtree + number of elements in right-subtree + locally searched elements) +
                                O(log(number of elements in middle subtree))

Explanation:
Big-O of number of elements in right & left subtree PLUS elements searched in bounded search space AND
Big-O of log of number of elements in middle tree subtree; as searched as binary search tree

Generic approach-

Aim 1: Given the height of the tree, find the maximum absolute difference between the adjacent vertices.

Steps:
1. Find the number of nodes for the Totogram by adding up the nodes 3 balanced binary tree each with (height-1) as the height, with the root.
    Formula -> 3 * pow(2, (height - 1)  - 1) + 1.
2. To form the Totogram, root of the tree can be element on midpoint or midpoint + 1,
    can use either of them as number of elements to either sides of the chosen root will be reversed/symmetric.
3. Starting with midpoint as the root, reach both ends of the list of numbers with BOTH of the following condition 1 & 2, to be TRUE.

Condition 1: Try to stretch out the left most branch of the left sub-tree to reach to the lowest number,
            such that <<depth from root to the lowest number in the list = height of the Totogram>>

Condition 2: Similarly, try to stretch out the right most branch of the right sub-tree to reach to the highest number,
            such that <<depth from the root to the highest number in the list = height of the Totogram>>
4. Iteratively repeat Step 3 for different value of differences starting from 1.

Explanation:

Stretching the branch refers to;
For left sub-tree -

<<value of left child at depth 1>> = <<value of root node>> - difference
<<value of left child at depth 2>> = <<value of parent at depth 1>> - difference
<<value of left child at depth 3>> = <<value of parent at depth 2>> - difference

and so on.. till <<value of the left child at depth n>> is lesser or equal to LOWEST number,

The number of subtractions performed above indicates the depth from root to the LOWEST number,

If number of subtractions > height; condition 1 is NOT MET, pick next difference

For right sub-tree -

<<value of right child at depth 1>> = <<value of root node>> + difference
<<value of right child at depth 2>> = <<value of parent at depth 1>> + difference
<<value of right child at depth 3>> = <<value of parent at depth 2>> + difference

and so on.. till <<value of the right child at depth n>> is greater or equal to GREATEST number

The number of additions performed above indicates the depth from root to the GREATEST number,

If number of additions > height; condition 2 is NOT MET, pick next difference

Perform this step, till first difference which satisfies the condition is found.

Logic:

Keeping constraints of the height, take the best possible step to the next node and so on. to reach the end numbers.

Example: for given height = 3; root = 5; #nodes = 10

difference 1,
left-most branch; depth > height [X]
       5
     4
   3
 2
1

difference 2,
left-most branch; depth(3) = height(3); [0]
       5
     3
   1
right-most branch, depth(4) > height(3) [X]
5
 7
  9
   10

difference 3,
left-most branch; depth(3) = height(3); [0]
       5
     2
   1
right-most branch, depth(3) = height(3) [0]
5
 8
  10

Hence, maximum absolute difference between the nodes is 3. As we are able to reach to both the end nodes from the root with depth same as the given height.
This also proves that if we can reach the ends with this difference then we can reach any of the remaining numbers with adjacent vertex difference lesser than or equal to the found maximum difference.


Aim 2: Construct the left most balanced tree

Steps:
[difference(diff) = - maximum difference]
1. Using the maximum difference found from Aim 1, form the left balanced sub-tree.
2. Add left and right child through bounded local search, with maximum difference as the upper bound.
2.1. DFS (left-skied) from the root to LOWEST number with max. difference
2.2. Recursively add right child - find the first available element from parent at distances of diff/diff+ 1/diff+ 2../-1. [L->R]
    If none found pick the first element from START the list of available numbers
2.3. Recursively add left child, find the first available element from START the list of available numbers [ascending order, unvisited nodes]

Example, for height = 4, difference = 4, number of nodes = 22
          11 <-root
       7
    3      4
 1    2  5   6

Aim 3: Construct the right most balanced tree

Steps:
[difference(diff) = maximum difference]
Similar to Aim 2,

1. Using the maximum difference found from Aim 1, form the right balanced sub-tree.
2. Add left and right child through bounded local search, with maximum difference as the upper bound.
2.1. DFS (right-skied) from the root to GREATEST number with max. difference
2.2. Recursively add left child - find the first available element from parent at distances of diff/diff- 1/diff-2../1. [L->R]
    If none found pick the first element from END of list of available numbers
2.3. Recursively add right child, find the first element from END of list of available numbers [ascending order, unvisited nodes]

Example
              11 <-root
                 15
             18      19
          20    17 21   22


Logic for Aim 2 & 3:

The conditions for adding node are formed because ..

1. Need to fit in as many numbers in the right and left sub-tree
2. For left sub-tree, priority given to the smaller available numbers as coz if we don't pick them now they'll be further away from the numbers within the range of maximum difference found
3. Similar for right sub-tree, larger available numbers

Aim 4: Construct the balanced tree in the middle

Steps:
1. With the list of remaining numbers, build the middle sub-tree.

2. Recursively pick the element at the midpoint for both sides of the parent, and form the sub tree.

Example, The remaining numbers for the above tree,

8, 9, 10, [12], 13, 14, 16 <- root

8, <9>, 10, [12], 13, <14>, 16 <- level 1, midpoints on either side of previous level

{8}, <9>, {10}, [12], {13}, <14>, {16} <- level 2, midpoints on either side of previous level

Logic:
1. As most of the elements which are closer to both ends, are taken by left and right most balanced tree.,
2. The remaining elements are within best difference from the chosen midpoints of the parent.

Aim 5: Merge left, middle and right sub-tree with root to generate Totogram

'''
import sys
import copy
import math
import time

class Totogram:
    # initialize variables and calculate number of nodes and midpoint
    def __init__(self, height):
        self.height = height
        self.nodeCount = 3 * (pow(2, height - 1) - 1) + 1
        self.midpoint = self.nodeCount / 2  # as number of nodes will always be even
        self.maxDifference = 0
        self.root = 0
        self.remainingElements = []
        self.leftBranch = []
        self.rightBranch = []
        self.middleBranch = []
        self.branch = []
        self.tree = []

    # check left-most branch for left sub-tree and check right-most branch for right sub-tree. DFS on both ends.
    def checkBranch(self, difference):
        currNode = self.midpoint
        levelCount = 1
        while 0 < currNode < self.nodeCount:
            currNode += difference
            levelCount += 1
        return levelCount <= self.height

    # find the least value of maximum absolute difference between adjacent nodes
    def findMaxDifference(self):
        for maxDiff in range(1, self.midpoint+1):
            if self.checkBranch(-maxDiff) and \
                    self.checkBranch(maxDiff):
                self.maxDifference = maxDiff
                break

    # construct branches for middle subTree
    def constructMiddleSubTree(self, parent, startIndex, endIndex, branchLeft):
        midPoint = int(math.ceil((endIndex + startIndex) / 2.0))
        nextElem = self.remainingElements[midPoint - 1]
        if parent == 0:
            self.branch[0] = nextElem
        elif branchLeft:
            self.branch[int(2 * (self.branch.index(parent) + 1) - 1)] = nextElem
        else:
            self.branch[int(2 * (self.branch.index(parent) + 1) + 1 - 1)] = nextElem
        if startIndex == endIndex:
            return
        self.constructMiddleSubTree(nextElem, startIndex, midPoint - 1, True)
        self.constructMiddleSubTree(nextElem, midPoint + 1, endIndex, False)

    # construct branches for left and right sub-tree
    def constructBranch(self, parent, branchLeft, depth, difference, count):
        if count == 0:
            return
        # find next available number to add to tree
        nextElem = 0
        checkElem = parent + difference
        if checkElem in self.remainingElements:
            nextElem = checkElem
        else:
            # we need to find the next best number!
            if difference > 0 and branchLeft:
                diff = difference
                checkElem = 0
                while diff != 1:
                    diff -= 1
                    temp = parent + diff
                    if temp in self.remainingElements:
                        checkElem = parent + diff
                        break
                if checkElem == 0:
                    nextElem = self.remainingElements[-1]
                else:
                    nextElem = checkElem
            elif difference < 0 and branchLeft:
                nextElem = self.remainingElements[0]

            elif difference > 0 and not branchLeft:
                nextElem = self.remainingElements[-1]

            elif difference < 0 and not branchLeft:
                diff = difference
                checkElem = 0
                while diff != -1:
                    diff += 1
                    temp = parent + diff
                    if temp in self.remainingElements:
                        checkElem = temp
                        break
                if checkElem == 0:
                    nextElem = self.remainingElements[0]
                else:
                    nextElem = checkElem

        parentIndex = (self.branch.index(parent) + 1)

        if branchLeft:
            self.branch[int(2 * (parentIndex) - 1)] = nextElem
        else:
            self.branch[int(2 * (parentIndex) - 1 + 1)] = nextElem

        self.remainingElements.pop(self.remainingElements.index(nextElem))
        # if difference < 0:
        if depth + 2 >= self.height:
            if not (self.branch[(2 * parentIndex) - 1] != None and self.branch[2 * parentIndex] != None):
                # leaf node reached, go to parent and right
                parent, depth, count = self.constructBranch(parent, not branchLeft, depth, difference, count - 1)
            else:
                count -= 1
        elif depth + 2 < self.height:
            parent, depth, count = self.constructBranch(nextElem, branchLeft, depth + 1, difference, count - 1)
        return parent, depth, count

    # construct left, middle and right sub-trees
    def processSubTree(self, difference, branchLeft):
        self.branch = [None for i in range(0, pow(2, self.height - 1) - 1)]

        # If difference is Zero, construct middle branch
        if difference == 0:
            startIndex = 1
            endIndex = len(self.remainingElements)
            midPoint = int(math.ceil((endIndex + startIndex) / 2.0))
            parent = self.remainingElements[midPoint - 1]
            self.branch[0] = parent
            self.constructMiddleSubTree(0, startIndex, endIndex, True)
        else:
            self.branch[0] = self.root + difference
            if self.branch[0] in self.remainingElements:
                self.remainingElements.remove(self.branch[0])
            else:
                # for height = 2;
                self.branch[0] = self.remainingElements.pop(0)
            # extra -1 as parent/root node of the subtree is added
            count = pow(2, self.height - 1) - 1 - 1
            depth = 2
            parent = self.branch[0]
            while count != 0:
                parent, depth, count = self.constructBranch(parent, branchLeft, depth - 1, difference, count)
                while True and count != 0:
                    parentIndex = int(math.floor((self.branch.index(parent) + 1) / 2.0) - 1)
                    parent = self.branch[parentIndex]
                    if self.branch[2 * (parentIndex + 1) - 1] == None:
                        branchLeft = True
                        break
                    elif self.branch[2 * (parentIndex + 1) - 1 + 1] == None:
                        branchLeft = False
                        break
                    depth -= 1

    # merge left, middle and right sub-tree to form totogram
    def mergeSubTrees(self):
        startIndex = 0
        for depth in range(0, self.height):
            endIndex = startIndex + pow(2, depth)
            self.tree += self.leftBranch[startIndex:endIndex] + \
                         self.middleBranch[startIndex:endIndex] + \
                         self.rightBranch[startIndex:endIndex]
            startIndex = endIndex
        self.tree.insert(0, self.root)

    # construct Totogram; root and 3 balanced sub-trees
    def constructTotogram(self):

        # generate list of remaining elements/nodes of Totogram
        self.remainingElements = [i for i in range(1, self.nodeCount + 1)]

        # set root as midpoint of numbers
        self.root = self.midpoint

        # remove midpoint from list of remaining numbers
        self.remainingElements.pop(self.remainingElements.index(self.root))

        # Process Left Branch with negative Maximum Difference and branchLeft as True
        self.processSubTree(-self.maxDifference, branchLeft=True)
        self.leftBranch = copy.copy(self.branch)

        # Process Right Branch with positive Maximum Difference and branchLeft as False
        self.processSubTree(self.maxDifference, branchLeft=False)
        self.rightBranch = copy.copy(self.branch)

        # Process Middle Branch; dummy value for maximum difference and branchLeft
        self.processSubTree(0, branchLeft=False)
        self.middleBranch = copy.copy(self.branch)

        # Merge Left, Middle and Right branches to form Totogram, with midpoint as root
        self.mergeSubTrees()


    # draw sub-Trees; requires: pyDot
    def drawSubTree(self, graph, branch):
        import pydot
        count = 0
        parentList = [self.root]
        for depth in range(0, self.height - 1):
            nodeCount = 0;
            for nodeIndex in range(0, pow(2, depth)):
                nodeCount += 1
                child = branch[count + nodeIndex]
                if nodeCount % 2 == 1:
                    parent = parentList.pop(0)
                parentList.append(child)
                edge = pydot.Edge(str(parent), str(child))
                graph.add_edge(edge)
            count = count + nodeIndex + 1
        return graph

    # draw totogram; requires: pyDot
    def drawTotogram(self):
        import pydot
        graph = pydot.Dot(graph_type='graph')
        self.drawSubTree(graph, self.leftBranch)
        self.drawSubTree(graph, self.middleBranch)
        self.drawSubTree(graph, self.rightBranch)
        graph.write_png('Totogram - ' + str(self.height) + '.png')

def main():
    height = int(sys.argv[1])
    startTime = time.time()
    totogram = Totogram(height)
    totogram.findMaxDifference()
    totogram.constructTotogram()
    #totogram.drawTotogram()
    print "Time taken: ", round(time.time() - startTime, 8), "seconds"
    print totogram.maxDifference
    print ' '.join(map(str, totogram.tree))

if __name__ == '__main__':
    main()
