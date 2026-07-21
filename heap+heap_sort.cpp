//1-indexed
void Max_Heapify (vector<int> & A, int index) {
    int i = 2*index;
    int j = 2*index + 1;
    int largest;
    if (i < A.size() && A[i] > A[index]) {
        largest = i;
    } else {
        largest = index;
    }
    if (j < A.size() && A[j] > A[largest]) {
        largest = j;
    }
    if (largest != index) {
        swap(A[largest], A[index]);
        Max_Heapify(A, largest);
    }
}

//Build a heap from an existing array.
void build_max_heap(vector<int> & A) {
    for (int i = A.size()/2; i >= 1; --i) {
        Max_Heapify(A, i);
    }
}

void heap_sort(vector<int> &A) {
    int n = A.size() - 1;
    vector<int> B;
    while (n) {
        build_max_heap(A);
        B.push_back(A[1]);
        swap(A[1], A[n]);
        A.pop_back();
        n--;
    }
    A = B;
    return;
}
