function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
    %GRADIENTDESCENT Performs gradient descent to learn theta
    %   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by
    %   taking num_iters gradient steps with learning rate alpha

    % Initialize some useful values
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1);

    for iter = 1:num_iters
        % ====================== YOUR CODE HERE ======================
        % Instructions: Perform a single gradient step on the parameter vector
        %               theta.
        %
        % Hint: While debugging, it can be useful to print out the values
        %       of the cost function (computeCost) and gradient here.
        % X = m samples by n plus 1 features
        % theta = n plus 1 features in size
        % h = m by 1 vector containing the predictions
        h = (X*theta);
        % computing omega for the gradient descent formula:
        %%%%%%  theta = theta - alpha*derivative-of-cost-function
        % remember - cost function is : 1/(2m) * sum((X*theta - y)^2)
        omega = (1/m)*sum((h - y).*X);
        theta = theta - alpha*omega(1, :)';
        % ============================================================

        % Save the cost J in every iteration
        J_history(iter) = computeCost(X, y, theta);
    end

end
