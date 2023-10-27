package kr.ac.kookmin.udclasses;

public class Order {
	private DVD dvdsOrdered[] = new DVD[10]; // 배열변수 추가, DVD클래스의 인스턴스 변수로 배열변수를 선언.
	private int numOrdered = 0;
	/**
	 * @return the numOrdered
	 */
	public int getNumOrdered() {
		return numOrdered;
	}
	/**
	 * @param numOrdered the numOrdered to set
	 */
	public void setNumOrdered(int numOrdered) {
		this.numOrdered = numOrdered;
	}
	public void addDVD(DVD disc) {
		int qty = getNumOrdered();
		if(qty < 10) {
			dvdsOrdered[qty] = disc;
			setNumOrdered(qty + 1);
		}
	}
	public float totalCost() {
		int num = getNumOrdered();
		float total = 0;
		for(int i=0; i<num; i++) {
			total = total + dvdsOrdered[i].getCost(); // DVD클래스의 배열변수인 dvdsOrdered[].getCost() DVD클래스의 메소드를 사용.
		}
		return total; // void메쏘드는 값을 return하지 못한다. 특정 타입을 가진 메쏘드는 해당 타입의 값으로 return 할 수 있다.
	}
	public void removeDVD(DVD disc) {
		int qty = getNumOrdered();
		if(qty > 0) {
			for(int i=0; i<qty; i++) {
				if(disc.equals(dvdsOrdered[i])) {
					dvdsOrdered[i] = null;
					setNumOrdered(qty-1);
					break;
				}
			}
		}
	}
	
}
