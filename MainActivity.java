
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText num1, num2;
    TextView result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num1 = findViewById(R.id.num1);
        num2 = findViewById(R.id.num2);
        result = findViewById(R.id.result);
    }

    public void add(View view) {
        calculate('+');
    }

    public void subtract(View view) {
        calculate('-');
    }

    public void multiply(View view) {
        calculate('*');
    }

    public void divide(View view) {
        calculate('/');
    }

    void calculate(char op) {
        String a = num1.getText().toString();
        String b = num2.getText().toString();

        if (a.isEmpty() || b.isEmpty()) {
            Toast.makeText(this, "Enter both numbers",
                    Toast.LENGTH_SHORT).show();
            return;
        }

        double x = Double.parseDouble(a);
        double y = Double.parseDouble(b);
        double ans = 0;

        if (op == '+')
            ans = x + y;
        else if (op == '-')
            ans = x - y;
        else if (op == '*')
            ans = x * y;
        else if (op == '/') {
            if (y == 0) {
                result.setText("Cannot divide by zero");
                return;
            }
            ans = x / y;
        }

        result.setText("Result: " + ans);
    }
}
