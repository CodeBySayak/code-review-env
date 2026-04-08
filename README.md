# Code Review & Security Analysis Environment

## Overview
This project implements a real-world OpenEnv environment where an AI agent performs code review and identifies bugs and security vulnerabilities.

The agent analyzes code snippets and takes appropriate actions such as approving, rejecting, or flagging security risks.

---

## Objective
Simulate real-world software engineering workflows where automated systems assist in code review and security auditing.

---

## Observation Space
Each observation contains:

- **title**: Short description of the code issue  
- **code**: Code snippet to analyze  
- **goal**: Task description  

---

## Action Space

The agent can take one of the following actions:

- `approve` → Code is safe  
- `request_changes` → Minor issues  
- `reject` → Major issues  
- `flag_security` → Security vulnerability detected  

---

## Tasks

### Easy
- Detect obvious issues like hardcoded passwords  

### Medium
- Identify vulnerabilities like SQL injection  

### Hard
- Detect critical risks like remote code execution (`eval`)  

---

## Reward Function

- **1.0** → Correct action  
- **0.0** → Incorrect action  
- **-1.0** → Dangerous decision (e.g., approving unsafe code)  

---

## Setup Instructions

1. Install dependencies:
2. Set environment variable:
3. Run inference:

---

## Baseline Results

Score: 1.0
Score: 1.0
Score: 1.0
Average: 1.0


---

## Deployment

The environment is deployed using Hugging Face Spaces with Docker support.

---

## Key Features

- Real-world code review simulation  
- Multi-level task difficulty  
- Security-focused evaluation  
- Compatible with OpenAI client API  

---
