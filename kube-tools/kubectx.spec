Name:           kubectx
Version:        0.9.5
Release:        1%{?dist}
Summary:        EOG Power tools for kubetcl

License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectx
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  bash
Requires:       bash
Requires:       kubectl
BuildArch:      noarch

%description
kubectx is a tool to switch between contexts (clusters) on kubectl faster.


%package -n kubens
Summary:        EOG Power tools for kubectl
Requires:       bash
Requires:       kubectl
%description -n kubens
kubens is a tool to switch between Kubernetes namespaces (and configure them for kubectl) easily.


%prep
%autosetup %{name}-v%{version}


%build
# nothing to build


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 kubens %{buildroot}%{_bindir}/kubens


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%files -n kubens
%license LICENSE
%doc README.md
%{_bindir}/kubens


%changelog
* Mon Oct 28 2024 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.9.5-1
- Initial build
