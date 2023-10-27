package Lab07;

public class Student {
	public int score;
	public String name;

	public Student(String name, int score) {
		this.name = name;
		this.score = score;
	}
	public String getName() {
		return name;
	}
	public void setName(String name_){
		name = name_;
	}
	public int getScore() {
		return score;
	}
	public void setScore(int score_) {
		score = score_;
	}
}
