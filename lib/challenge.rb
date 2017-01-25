# Requirements

def any?(array, &block)
  array.any?(&block)
end

def none?(array, &block)
  array.none?(&block)
end

# Bonuses

def one?(array, &block)
  array.one?(&block)
end

def all?(array, &block)
  array.all?(&block)
end
