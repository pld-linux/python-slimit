#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module slimit
Summary:	JavaScript minifier written in Python
Name:		python-slimit
Version:	0.7.4
Release:	4
License:	MIT
Group:		Development/Languages
URL:		http://slimit.org/
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.zip
# Source0-md5:	35b50859883a1d8dfd61a77c125f517d
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
%if %{with tests}
BuildRequires:	python-odict
BuildRequires:	python-ply >= 3.4
%endif
Requires:	python-odict
Requires:	python-ply >= 3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SlimIt is a JavaScript minifier written in Python. It compiles
JavaScript into more compact code so that it downloads and runs
faster.

SlimIt also provides a library that includes a JavaScript parser,
lexer, pretty printer and a tree visitor.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
%{__python} setup.py test -m slimit.tests.test_lexer
%{__python} setup.py test -m slimit.tests.test_nodevisitor
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/slimit/tests

%py_postclean

chmod a+x $RPM_BUILD_ROOT%{_bindir}/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.rst
%attr(755,root,root) %{_bindir}/slimit
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/visitors
%{py_sitescriptdir}/%{module}/visitors/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
